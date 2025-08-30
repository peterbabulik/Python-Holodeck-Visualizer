import React, { useRef, useEffect } from 'react';
import { useFrame, useThree } from '@react-three/fiber';
import { OrbitControls, FlyControls } from '@react-three/drei';
import * as THREE from 'three';
import { useCodeGraphStore } from '../../hooks/useCodeGraphStore';

const CameraManager: React.FC = () => {
  // FIX: Subscribed to state slices individually using selectors.
  // This is a Zustand best practice for performance and likely resolves the "Expected 1 arguments, but got 0" error,
  // which probably refers to this hook call missing a selector argument.
  const cameraMode = useCodeGraphStore((state) => state.cameraMode);
  const activeNodeId = useCodeGraphStore((state) => state.activeNodeId);
  const graphData = useCodeGraphStore((state) => state.graphData);
  const isTracing = useCodeGraphStore((state) => state.isTracing);
  const { camera, gl } = useThree();
  const controlsRef = useRef<any>();
  const targetPosition = useRef(new THREE.Vector3());
  const isUserInteracting = useRef(false);

  useEffect(() => {
    const onInteractionStart = () => { isUserInteracting.current = true; };
    const onInteractionEnd = () => { isUserInteracting.current = false; };
    
    gl.domElement.addEventListener('pointerdown', onInteractionStart, false);
    gl.domElement.addEventListener('pointerup', onInteractionEnd, false);
    gl.domElement.addEventListener('wheel', onInteractionStart, false);

    const timeout = setTimeout(() => { isUserInteracting.current = false; }, 2000);

    return () => {
      gl.domElement.removeEventListener('pointerdown', onInteractionStart);
      gl.domElement.removeEventListener('pointerup', onInteractionEnd);
      gl.domElement.removeEventListener('wheel', onInteractionStart);
      clearTimeout(timeout);
    };
  }, [gl.domElement]);

  useFrame((_, delta) => {
    if ((cameraMode === 'observe' || (isTracing && cameraMode === 'orbit')) && activeNodeId && !isUserInteracting.current) {
      const activeNode = graphData?.nodes.find(n => n.id === activeNodeId);
      if (activeNode) {
        targetPosition.current.set(...activeNode.position);
        
        const idealOffset = new THREE.Vector3(0, 5, 15);
        const idealPosition = new THREE.Vector3().addVectors(targetPosition.current, idealOffset);
        
        camera.position.lerp(idealPosition, delta * 1.5);
        
        const tempLookAt = new THREE.Vector3();
        if(controlsRef.current?.target) {
            tempLookAt.copy(controlsRef.current.target);
        }
        tempLookAt.lerp(targetPosition.current, delta * 2);
        camera.lookAt(tempLookAt);
        if(controlsRef.current?.target) {
            controlsRef.current.target.copy(tempLookAt);
        }
      }
    }
  });

  return (
    <>
      {cameraMode === 'orbit' && <OrbitControls ref={controlsRef} args={[camera, gl.domElement]} enableDamping dampingFactor={0.1} rotateSpeed={0.5} />}
      {cameraMode === 'static' && <OrbitControls ref={controlsRef} args={[camera, gl.domElement]} enableDamping dampingFactor={0.1} enableRotate={false} />}
      {cameraMode === 'fly' && <FlyControls ref={controlsRef} movementSpeed={5} rollSpeed={Math.PI / 12} dragToLook />}
      {cameraMode === 'observe' && <OrbitControls ref={controlsRef} args={[camera, gl.domElement]} enableDamping dampingFactor={0.1} />}
    </>
  );
};

export default CameraManager;
