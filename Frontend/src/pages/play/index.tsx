import Link from 'next/link'
import  PlayComponent from '../../components/play'

export default function Play({ }) {
  return (
    <>
      <div>
        Play
      </div>

      <PlayComponent promptId={undefined}/>

      <Link href="/">
        Home
      </Link>
    </>
    )
}
  