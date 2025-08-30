
import { create } from 'zustand';
import { GraphData, ExecutionTrace, ExecutionStatus, CameraMode } from '../types';
import { generateGraphFromCode } from '../services/geminiService';

interface CodeGraphState {
  graphData: GraphData | null;
  executionTrace: ExecutionTrace | null;
  currentStep: number;
  activeNodeId: number | null;
  isTracing: boolean;
  executionSpeed: number;
  cameraMode: CameraMode;
  status: ExecutionStatus;
  error: string | null;
  fileName: string | null;

  loadCode: (code: string, fileName: string) => Promise<void>;
  startTrace: () => void;
  stopTrace: () => void;
  resetTrace: () => void;
  nextStep: () => void;
  setExecutionSpeed: (speed: number) => void;
  setCameraMode: (mode: CameraMode) => void;
}

export const useCodeGraphStore = create<CodeGraphState>((set, get) => ({
  graphData: null,
  executionTrace: null,
  currentStep: -1,
  activeNodeId: null,
  isTracing: false,
  executionSpeed: 0.6, // Base delay in seconds
  cameraMode: 'orbit',
  status: 'idle',
  error: null,
  fileName: null,

  loadCode: async (code: string, fileName: string) => {
    set({ status: 'loading', error: null, graphData: null, executionTrace: null, fileName });
    try {
      const { graph, trace } = await generateGraphFromCode(code);
      set({
        graphData: graph,
        executionTrace: trace,
        status: 'ready',
        currentStep: -1,
        activeNodeId: null,
        isTracing: false,
      });
    } catch (e) {
      const errorMessage = e instanceof Error ? e.message : 'An unknown error occurred.';
      set({ status: 'error', error: `Failed to process code. ${errorMessage}` });
    }
  },

  startTrace: () => {
    if (get().status === 'finished') {
        get().resetTrace();
    }
    set({ isTracing: true, status: 'tracing' });
    const traceInterval = () => {
      if (!get().isTracing) return;
      get().nextStep();
      if (get().isTracing) {
        setTimeout(traceInterval, get().executionSpeed * 1000);
      }
    };
    setTimeout(traceInterval, get().executionSpeed * 1000);
  },
  
  stopTrace: () => {
    set({ isTracing: false });
  },

  resetTrace: () => {
    set({
        currentStep: -1,
        activeNodeId: null,
        isTracing: false,
        status: 'ready'
    });
  },

  nextStep: () => {
    set(state => {
      if (!state.executionTrace) return {};
      const nextStep = state.currentStep + 1;
      if (nextStep >= state.executionTrace.length) {
        return { isTracing: false, status: 'finished', activeNodeId: null };
      }
      return {
        currentStep: nextStep,
        activeNodeId: state.executionTrace[nextStep],
      };
    });
  },

  setExecutionSpeed: (delay: number) => {
    set({ executionSpeed: delay });
  },

  setCameraMode: (mode: CameraMode) => {
    set({ cameraMode: mode });
  },
}));
