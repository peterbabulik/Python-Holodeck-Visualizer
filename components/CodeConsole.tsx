import React, { useEffect, useRef } from 'react';
import { useCodeGraphStore } from '../hooks/useCodeGraphStore';

const CodeConsole: React.FC = () => {
  const graphData = useCodeGraphStore((state) => state.graphData);
  const activeNodeId = useCodeGraphStore((state) => state.activeNodeId);
  const activeLineRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (activeLineRef.current) {
      activeLineRef.current.scrollIntoView({
        behavior: 'smooth',
        block: 'center',
      });
    }
  }, [activeNodeId]);

  if (!graphData) {
    return null;
  }

  // Sort nodes by line number to ensure correct display order
  const sortedNodes = [...graphData.nodes].sort((a, b) => a.id - b.id);

  return (
    <div className="absolute top-1/2 right-4 -translate-y-1/2 bg-black bg-opacity-70 p-4 rounded-lg w-1/4 max-w-md h-3/4 max-h-[700px] overflow-y-auto font-mono text-sm text-white border border-gray-700 backdrop-blur-sm">
      <h3 className="text-lg font-bold mb-4 text-blue-400 sticky top-0 bg-black bg-opacity-70 py-2 -mx-4 px-4 z-10">Execution Log</h3>
      <div className="pt-2">
        {sortedNodes.map(node => (
          <div
            key={node.id}
            ref={node.id === activeNodeId ? activeLineRef : null}
            className={`flex items-start p-1 rounded transition-colors duration-300 ${node.id === activeNodeId ? 'bg-blue-800 bg-opacity-50' : 'hover:bg-gray-700/50'}`}
          >
            <span className="w-8 text-gray-500 select-none">{node.id}</span>
            <pre className="whitespace-pre-wrap break-words flex-1">{node.code || '\n'}</pre>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CodeConsole;
