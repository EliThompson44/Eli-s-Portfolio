import './globals.css'
import Link from 'next/link'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header className="border-b border-slate-700 bg-slate-900/80 p-4">
          <nav className="mx-auto flex max-w-6xl gap-4 text-sm">
            <Link href="/">Dashboard</Link>
            <Link href="/players">Players</Link>
            <Link href="/timeline">Timeline</Link>
            <Link href="/draft">Draft</Link>
            <Link href="/compare">Compare</Link>
          </nav>
        </header>
        <main className="mx-auto max-w-6xl p-6">{children}</main>
      </body>
    </html>
  )
}
