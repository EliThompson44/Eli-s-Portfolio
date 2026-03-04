export default function ComparePage() {
  return (
    <section className="space-y-3 card">
      <h1 className="text-2xl font-bold">Player Comparison Tool</h1>
      <p>Use API endpoint <code>/api/analytics/player-comparison/{'{idA}'}/{'{idB}'}</code> to compare two players by legacy score.</p>
      <p>This page is intentionally lightweight for fast manual franchise workflows and can be expanded into interactive charts.</p>
    </section>
  )
}
