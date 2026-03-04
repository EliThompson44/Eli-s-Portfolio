const seasons = [
  { year: 1960, champion: "Boston Royals", mvp: "J. Carter" },
  { year: 1985, champion: "Chicago Steel", mvp: "A. Rhodes" },
  { year: 2027, champion: "Seattle Emeralds", mvp: "M. Iverson" },
];

export default function TimelinePage() {
  return (
    <main className="mx-auto max-w-5xl px-6 py-10">
      <h1 className="text-3xl font-bold">Season Timeline Explorer</h1>
      <ul className="mt-6 space-y-3">
        {seasons.map((season) => (
          <li key={season.year} className="rounded-lg border border-slate-800 bg-slate-900 p-4">
            <p className="font-semibold">{season.year}</p>
            <p className="text-sm text-slate-300">Champion: {season.champion} · MVP: {season.mvp}</p>
          </li>
        ))}
      </ul>
    </main>
  );
}
