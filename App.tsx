
import React, { useCallback, useRef } from 'react';
import { useCodeGraphStore } from './hooks/useCodeGraphStore';
import HolodeckCanvas from './components/HolodeckCanvas';
import ControlPanel from './components/ControlPanel';
import Loader from './components/Loader';
import { FileCodeIcon, UploadIcon } from './components/Icons';
import CodeConsole from './components/CodeConsole'; // Import the new component

const App: React.FC = () => {
  const { status, error, loadCode, fileName } = useCodeGraphStore();
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = useCallback((event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const content = e.target?.result as string;
        loadCode(content, file.name);
      };
      reader.readAsText(file);
    }
  }, [loadCode]);

  const handleUploadClick = () => {
    fileInputRef.current?.click();
  };

  const renderContent = () => {
    switch (status) {
      case 'loading':
        // Updated loader message
        return <Loader message="Analyzing Python code..." />;
      case 'error':
        return (
          <div className="flex flex-col items-center justify-center h-full text-white text-center">
            <h2 className="text-2xl font-bold text-red-500 mb-4">Analysis Failed</h2>
            <p className="max-w-md mb-6">{error}</p>
            <button
              onClick={handleUploadClick}
              className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg flex items-center transition-colors"
            >
              <UploadIcon className="h-5 w-5 mr-2" />
              Try Another File
            </button>
          </div>
        );
      case 'idle':
        return (
          <div className="absolute inset-0 flex items-center justify-center bg-gray-900 bg-opacity-80 z-10">
            <div className="text-center text-white p-8 max-w-2xl bg-black bg-opacity-30 backdrop-blur-sm rounded-2xl border border-gray-700">
              <h1 className="text-4xl font-bold mb-4 text-blue-400">Python Holodeck Visualizer</h1>
              <p className="mb-8 text-gray-300">
                Upload a Python script to generate an interactive 3D graph of its structure and trace the execution flow step-by-step.
              </p>
              <input
                type="file"
                ref={fileInputRef}
                onChange={handleFileChange}
                className="hidden"
                accept=".py"
              />
              <button
                onClick={handleUploadClick}
                className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg text-lg flex items-center mx-auto transition-transform hover:scale-105"
              >
                <UploadIcon className="h-6 w-6 mr-3" />
                Select Python File
              </button>
            </div>
          </div>
        );
      case 'ready':
      case 'tracing':
      case 'finished':
        return (
          <>
            <HolodeckCanvas />
            <ControlPanel />
            <CodeConsole /> 
            <div className="absolute top-4 left-4 text-white bg-black bg-opacity-50 px-3 py-2 rounded-lg text-sm flex items-center">
                <FileCodeIcon className="h-4 w-4 mr-2 text-blue-400"/>
                {fileName}
            </div>
          </>
        );
      default:
        return null;
    }
  };

  return (
    <div className="w-screen h-screen bg-gray-900 text-white">
      {renderContent()}
    </div>
  );
};

export default App;
