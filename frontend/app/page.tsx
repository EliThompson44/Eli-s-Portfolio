import { DashboardCard } from "@/components/dashboard-card";
import { PlayerTable } from "@/components/player-table";

const teams = [
  {
    name: "Seattle Emeralds",
    systemStyle: "Seven Seconds or Less",
    championships: 4,
    playoffAppearances: 12,
    legacyScore: 872,
    hallOfFamers: 5,
  },
  {
    name: "Chicago Steel",
    systemStyle: "Triangle Offense",
    championships: 6,
    playoffAppearances: 19,
    legacyScore: 1210,
    hallOfFamers: 8,
  },
];

export default function HomePage() {
  return (
    <main className="mx-auto flex min-h-screen max-w-6xl flex-col gap-8 px-6 py-10">
      <div>
        <h1 className="text-4xl font-bold">NBA Legacy Universe Tracker</h1>
        <p className="mt-2 text-slate-300">Franchise dashboard, player history, and alternate timeline analytics from 1960 onward.</p>
      </div>

      <section className="grid gap-4 md:grid-cols-4">
        <DashboardCard label="Total Seasons" value={68} />
        <DashboardCard label="Players Tracked" value={10124} />
        <DashboardCard label="Active Dynasties" value={2} />
        <DashboardCard label="League Storylines" value={136} />
      </section>

      <section className="rounded-xl border border-slate-800 bg-slate-900 p-5">
        <h2 className="mb-4 text-xl font-semibold">Franchise Dashboard</h2>
        <div className="grid gap-3 md:grid-cols-2">
          {teams.map((team) => (
            <div key={team.name} className="rounded-lg border border-slate-800 bg-slate-950 p-4">
              <h3 className="text-lg font-semibold">{team.name}</h3>
              <p className="text-sm text-cyan-300">{team.systemStyle}</p>
              <div className="mt-3 grid grid-cols-2 gap-2 text-sm text-slate-300">
                <p>🏆 Championships: {team.championships}</p>
                <p>🎯 Playoffs: {team.playoffAppearances}</p>
                <p>📈 Legacy Score: {team.legacyScore}</p>
                <p>⭐ Hall of Fame: {team.hallOfFamers}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section>
        <h2 className="mb-3 text-xl font-semibold">Player Database</h2>
        <PlayerTable />
      </section>
    </main>
  );
}
