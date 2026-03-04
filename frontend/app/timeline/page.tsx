import { getJSON } from '@/lib/api'

type Season = { id: number; year: number; finals_matchup?: string; key_storyline_1?: string; key_storyline_2?: string; draft_class_summary?: string; major_trades?: string }

export default async function TimelinePage() {
  const seasons = await getJSON<Season[]>('/seasons', [])
  return (
    <section className="space-y-4">
      <h1 className="text-2xl font-bold">Season Timeline Explorer</h1>
      {seasons.map((s) => (
        <article key={s.id} className="card space-y-1">
          <h2 className="text-lg font-semibold">{s.year} Season</h2>
          <p>Finals: {s.finals_matchup || 'TBD'}</p>
          <p>Draft Class: {s.draft_class_summary || 'Not entered'}</p>
          <p>Major Trades: {s.major_trades || 'Not entered'}</p>
          <p>Storyline 1: {s.key_storyline_1 || 'Pending'}</p>
          <p>Storyline 2: {s.key_storyline_2 || 'Pending'}</p>
        </article>
      ))}
    </section>
  )
}
