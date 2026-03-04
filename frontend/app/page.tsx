import { getJSON } from '@/lib/api'

type Team = { id: number; name: string; system_style: string; championships: number; playoff_appearances: number; legacy_score: number }

const styles = [
  'Grit and Grind',
  'Run and Gun',
  'Triangle Offense',
  'Defense First',
  'Seven Seconds or Less',
  'Inside Dominance',
  '3 Point Revolution',
]

export default async function HomePage() {
  const teams = await getJSON<Team[]>('/teams', [])

  return (
    <section className="space-y-6">
      <h1 className="text-3xl font-bold">NBA Legacy Universe Tracker</h1>
      <div className="grid gap-4 md:grid-cols-4">
        {teams.slice(0, 8).map((team) => (
          <article key={team.id} className="card">
            <h2 className="font-semibold">{team.name}</h2>
            <p className="text-sm text-slate-300">{team.system_style}</p>
            <ul className="mt-3 text-sm">
              <li>🏆 Championships: {team.championships}</li>
              <li>🎟️ Playoffs: {team.playoff_appearances}</li>
              <li>📜 Legacy Score: {team.legacy_score}</li>
            </ul>
          </article>
        ))}
      </div>
      <article className="card">
        <h2 className="text-xl font-semibold">Supported System Styles</h2>
        <p className="mt-2 text-sm text-slate-300">Use these team tactical identities for franchise dashboards and fit analysis.</p>
        <div className="mt-3 flex flex-wrap gap-2">
          {styles.map((style) => (
            <span className="rounded-full bg-slate-700 px-3 py-1 text-xs" key={style}>{style}</span>
          ))}
        </div>
      </article>
    </section>
  )
}
