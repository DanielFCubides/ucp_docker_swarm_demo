import {getPing, getVisitors} from "@/services/reports";
import {Visits} from "@/app/(home)/components/visits/Visits";
import "./page.scss";

export default async function Home() {
  const visits = await getVisitors();
  const ping = await getPing();

  return (
    <div className="principal-widget">
        <h1>Hi Test, welcome back to Telesign!</h1>
        <p className="version-widget"><b>Version:</b> {ping.version} - <b>Timestamp</b>: {ping.timestamp}</p>
        <Visits visits={visits} />
    </div>
  );
}
