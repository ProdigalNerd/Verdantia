import { render, screen } from '@testing-library/react'
import App from '../App'

test('renders Verdantia header', () => {
  render(<App />)
  expect(screen.getByText(/Verdantia/i)).toBeInTheDocument()
})
