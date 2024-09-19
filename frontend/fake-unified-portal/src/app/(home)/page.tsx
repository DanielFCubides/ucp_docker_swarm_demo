import {getVisitors} from "@/services/reports";
import {Visits} from "@/app/(home)/components/visits/Visits";
import "./page.scss";

export default async function Home() {
  const visits = await getVisitors();

  return (
    <div className="principal-widget">
        <h1>Hi Test, welcome back to Telesign!</h1>
        <Visits visits={visits} />
    </div>
  );
}
