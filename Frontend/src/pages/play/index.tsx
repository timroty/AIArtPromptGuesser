import Link from 'next/link'
import  PlayComponent from '../../components/play'

export default function Play({ }) {
  return (
    <>
      <PlayComponent promptId={undefined}/>

      <Link href="/">
        Home
      </Link>
    </>
    )
}
  