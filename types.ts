
export interface GraphNode {
  id: number;
  code: string;
  position: [number, number, number];
}

export interface GraphEdge {
  source: number;
  target: number;
}

export interface GraphData {
  nodes: GraphNode[];
  edges: GraphEdge[];
}

export type ExecutionTrace = number[];

export type ExecutionStatus = 'idle' | 'loading' | 'ready' | 'tracing' | 'finished' | 'error';

export type CameraMode = 'orbit' | 'static' | 'fly' | 'observe';
