import create from 'zustand'

type GameState = {
  playerName: string | null
  setPlayerName: (name: string) => void
}

export const useGameStore = create<GameState>((set) => ({
  playerName: null,
  setPlayerName: (name: string) => set({ playerName: name })
}))
