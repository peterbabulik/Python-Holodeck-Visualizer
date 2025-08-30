
import React from 'react';
import { useCodeGraphStore } from '../hooks/useCodeGraphStore';
import { CameraMode } from '../types';
import { PlayIcon, PauseIcon, ResetIcon, OrbitIcon, PanIcon, FlyIcon, ObserveIcon } from './Icons';

const ControlPanel: React.FC = () => {
  const {
    status,
    isTracing,
    startTrace,
    stopTrace,
    resetTrace,
    executionSpeed,
    setExecutionSpeed,
    cameraMode,
    setCameraMode,
  } = useCodeGraphStore();

  const handleRunClick = () => {
    if (isTracing) {
      stopTrace();
    } else {
      startTrace();
    }
  };

  const handleResetClick = () => {
    resetTrace();
  };

  const speedOptions = [
    { label: '25%', value: 1.2 },
    { label: '50%', value: 0.9 },
    { label: '100%', value: 0.6 },
    { label: '200%', value: 0.3 },
  ];

  const cameraModes: { label: string, mode: CameraMode, icon: React.ReactNode }[] = [
    { label: 'Orbit', mode: 'orbit', icon: <OrbitIcon className="h-5 w-5" /> },
    { label: 'Static', mode: 'static', icon: <PanIcon className="h-5 w-5" /> },
    { label: 'Fly', mode: 'fly', icon: <FlyIcon className="h-5 w-5" /> },
    { label: 'Observe', mode: 'observe', icon: <ObserveIcon className="h-5 w-5" /> },
  ];

  const isControlsDisabled = status === 'loading';

  return (
    <div className="absolute bottom-4 left-1/2 -translate-x-1/2 flex flex-col items-center gap-4 z-10">
      {/* Camera and Speed Controls */}
      <div className="flex gap-4">
        {/* Camera Mode */}
        <div className="bg-black/50 backdrop-blur-sm p-2 rounded-lg flex items-center gap-1">
          {cameraModes.map(({ label, mode, icon }) => (
            <button
              key={mode}
              title={label}
              onClick={() => setCameraMode(mode)}
              disabled={isControlsDisabled}
              className={`px-3 py-2 rounded-md transition-colors text-sm flex items-center gap-2 ${
                cameraMode === mode ? 'bg-blue-600 text-white' : 'bg-gray-700/50 hover:bg-gray-600/50 text-gray-300'
              } disabled:opacity-50 disabled:cursor-not-allowed`}
            >
              {icon}
              <span className="hidden sm:inline">{label}</span>
            </button>
          ))}
        </div>

        {/* Speed Controls */}
        <div className="bg-black/50 backdrop-blur-sm p-2 rounded-lg flex items-center gap-1">
          {speedOptions.map(({ label, value }) => (
            <button
              key={value}
              onClick={() => setExecutionSpeed(value)}
              disabled={isControlsDisabled}
              className={`px-3 py-2 rounded-md transition-colors text-sm font-medium w-16 ${
                executionSpeed === value ? 'bg-blue-600 text-white' : 'bg-gray-700/50 hover:bg-gray-600/50 text-gray-300'
              } disabled:opacity-50 disabled:cursor-not-allowed`}
            >
              {label}
            </button>
          ))}
        </div>
      </div>
      
      {/* Main Execution Controls */}
      <div className="bg-black/50 backdrop-blur-sm p-2 rounded-full flex items-center gap-2">
        <button
          onClick={handleRunClick}
          disabled={isControlsDisabled || status === 'finished'}
          className="bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-full w-14 h-14 flex items-center justify-center transition-colors disabled:bg-gray-600 disabled:cursor-not-allowed"
        >
          {isTracing ? <PauseIcon className="h-7 w-7" /> : <PlayIcon className="h-7 w-7" />}
        </button>
        <button
          onClick={handleResetClick}
          disabled={isControlsDisabled}
          className="bg-gray-700 hover:bg-gray-600 text-white font-bold rounded-full w-14 h-14 flex items-center justify-center transition-colors disabled:opacity-50"
        >
          <ResetIcon className="h-6 w-6" />
        </button>
      </div>
    </div>
  );
};

export default ControlPanel;
