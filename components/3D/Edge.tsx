
import React from 'react';
import { Line } from '@react-three/drei';
import { GraphNode, GraphEdge as EdgeType } from '../../types';

interface EdgeProps {
  edge: EdgeType;
  nodes: GraphNode[];
}

const Edge: React.FC<EdgeProps> = ({ edge, nodes }) => {
  const sourceNode = nodes.find(n => n.id === edge.source);
  const targetNode = nodes.find(n => n.id === edge.target);

  if (!sourceNode || !targetNode) {
    return null;
  }

  return (
    <Line
      points={[sourceNode.position, targetNode.position]}
      color="#4b5563"
      lineWidth={1.5}
      dashed={false}
    />
  );
};

export default Edge;
