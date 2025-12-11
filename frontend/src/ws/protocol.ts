export type Envelope<T = unknown> = {
  v: number
  type: string
  id: string
  payload: T
}

export type ServerEvent = Envelope<{ message: string }>
export type ClientEvent = Envelope<{ action: string }>

export const PROTOCOL_VERSION = 1
