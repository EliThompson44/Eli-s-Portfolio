const players = [
  { name: "Eliot Barnes", pos: "SG", archetype: "3 and D Wing", ovr: 87, dev: "Late Bloomer" },
  { name: "Marcus Iverson", pos: "PG", archetype: "Playmaking Guard", ovr: 92, dev: "Linear Growth" },
  { name: "Darnell Price", pos: "C", archetype: "Defensive Anchor", ovr: 85, dev: "Early Peak" },
];

export function PlayerTable() {
  return (
    <div className="overflow-hidden rounded-xl border border-slate-800">
      <table className="min-w-full divide-y divide-slate-800 bg-slate-900 text-sm">
        <thead className="bg-slate-950 text-slate-400">
          <tr>
            <th className="px-4 py-3 text-left">Player</th>
            <th className="px-4 py-3 text-left">Pos</th>
            <th className="px-4 py-3 text-left">Archetype</th>
            <th className="px-4 py-3 text-left">OVR</th>
            <th className="px-4 py-3 text-left">Development</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-800">
          {players.map((player) => (
            <tr key={player.name}>
              <td className="px-4 py-3">{player.name}</td>
              <td className="px-4 py-3">{player.pos}</td>
              <td className="px-4 py-3">{player.archetype}</td>
              <td className="px-4 py-3">{player.ovr}</td>
              <td className="px-4 py-3">{player.dev}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
