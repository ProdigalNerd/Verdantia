import React from 'react'
import { useGameStore } from './state/useGameStore'

export default function App() {
  const state = useGameStore()
  return (
    <div>
      <h1>Verdantia</h1>
      <p>Player: {state.playerName || 'Anonymous'}</p>
    </div>
  )
}
