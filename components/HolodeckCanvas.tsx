
import React, { Suspense } from 'react';
import { Canvas } from '@react-three/fiber';
import { useCodeGraphStore } from '../hooks/useCodeGraphStore';
import CodeGraph from './3D/CodeGraph';
import CameraManager from './3D/CameraManager';

const HolodeckCanvas: React.FC = () => {
  const { graphData } = useCodeGraphStore();

  if (!graphData) return null;

  return (
    <Canvas camera={{ position: [0, 0, 30], fov: 75 }}>
      <color attach="background" args={['#111827']} />
      <ambientLight intensity={0.8} />
      <directionalLight position={[5, 10, 7.5]} intensity={1.5} />
      <pointLight position={[-5, -10, -5]} intensity={0.5} color="#87CEEB" />
      
      <Suspense fallback={null}>
        <CodeGraph graphData={graphData} />
      </Suspense>

      <CameraManager />
    </Canvas>
  );
};

export default HolodeckCanvas;
