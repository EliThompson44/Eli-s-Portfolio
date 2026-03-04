import { getJSON } from '@/lib/api'

type Prospect = { id: number; name: string; draft_year: number; expected_tier?: string; strengths?: string; weaknesses?: string }

export default async function DraftPage() {
  const prospects = await getJSON<Prospect[]>('/draft-prospects', [])
  return (
    <section className="space-y-4">
      <h1 className="text-2xl font-bold">Draft Analyzer</h1>
      <div className="grid gap-4 md:grid-cols-2">
        {prospects.map((prospect) => (
          <article key={prospect.id} className="card">
            <h2 className="font-semibold">{prospect.name} ({prospect.draft_year})</h2>
            <p>Expected Tier: {prospect.expected_tier}</p>
            <p className="text-sm text-green-300">Strengths: {prospect.strengths}</p>
            <p className="text-sm text-red-300">Weaknesses: {prospect.weaknesses}</p>
          </article>
        ))}
      </div>
    </section>
  )
}
