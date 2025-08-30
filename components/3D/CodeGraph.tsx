
import React from 'react';
import { GraphData } from '../../types';
import Node from './Node';
import Edge from './Edge';

interface CodeGraphProps {
  graphData: GraphData;
}

const CodeGraph: React.FC<CodeGraphProps> = ({ graphData }) => {
  return (
    <group>
      {graphData.nodes.map((node) => (
        <Node key={node.id} node={node} />
      ))}
      {graphData.edges.map((edge, index) => (
        <Edge key={`${edge.source}-${edge.target}-${index}`} edge={edge} nodes={graphData.nodes} />
      ))}
    </group>
  );
};

export default CodeGraph;
