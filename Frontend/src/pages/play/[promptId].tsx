import Link from 'next/link'
import { useRouter } from 'next/router';
import  PlayComponent from '../../components/play'

export default function Play({ }) {
  const router = useRouter();

  if (!router.isReady) {
    return null;
  } 

  return (
    <>

      <div>
        Play
      </div>

      <Link href="/">
        Home
      </Link>

      <PlayComponent promptId={router.query.promptId?.toString()}/>
    </>
    )
}


  