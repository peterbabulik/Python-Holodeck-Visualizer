
import React, { useRef, useMemo } from 'react';
import { useFrame } from '@react-three/fiber';
import { Text } from '@react-three/drei';
import * as THREE from 'three';
import { GraphNode } from '../../types';
import { useCodeGraphStore } from '../../hooks/useCodeGraphStore';

interface NodeProps {
  node: GraphNode;
}

const Node: React.FC<NodeProps> = ({ node }) => {
  const meshRef = useRef<THREE.Mesh>(null!);
  const { activeNodeId } = useCodeGraphStore();

  const isActive = activeNodeId === node.id;

  const targetColor = useMemo(() => {
    return isActive ? new THREE.Color('#f59e0b') : new THREE.Color('#3b82f6');
  }, [isActive]);

  useFrame(() => {
    if (meshRef.current) {
        const material = meshRef.current.material as THREE.MeshStandardMaterial;
        material.color.lerp(targetColor, 0.1);
    }
  });

  return (
    <group position={node.position}>
      <mesh ref={meshRef}>
        <sphereGeometry args={[0.5, 32, 32]} />
        <meshStandardMaterial color="#3b82f6" roughness={0.5} metalness={0.1} />
      </mesh>
      <Text
        position={[0.8, 0, 0]}
        color="white"
        fontSize={0.4}
        anchorX="left"
        anchorY="middle"
        outlineWidth={0.02}
        outlineColor="#000000"
      >
        {`${node.id}: ${node.code}`}
      </Text>
    </group>
  );
};

export default Node;
