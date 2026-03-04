import { getJSON } from '@/lib/api'

type Player = { id: number; name: string; position: string; draft_year: number; archetype: string; development_type: string; injury_risk: string; overall_rating: number }

export default async function PlayersPage() {
  const players = await getJSON<Player[]>('/players', [])
  return (
    <section className="space-y-4">
      <h1 className="text-2xl font-bold">Player Database</h1>
      <div className="overflow-x-auto card">
        <table className="w-full text-left text-sm">
          <thead className="text-slate-300">
            <tr>
              <th>Name</th><th>Pos</th><th>OVR</th><th>Archetype</th><th>Development</th><th>Injury Risk</th><th>Draft</th>
            </tr>
          </thead>
          <tbody>
            {players.map((p) => (
              <tr key={p.id} className="border-t border-slate-800">
                <td>{p.name}</td><td>{p.position}</td><td>{p.overall_rating}</td><td>{p.archetype}</td><td>{p.development_type}</td><td>{p.injury_risk}</td><td>{p.draft_year}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  )
}
