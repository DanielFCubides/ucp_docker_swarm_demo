import {getVisitors} from "@/services/reports";
import type {Visitors} from "@/services/reports";

export default async function Home() {
  const visits: Visitors = await getVisitors();

  return (
    <div>
      <h1>Visits</h1>
      <h1>visit count {visits.visit_count}</h1>
      <h1>local count {visits.local_visit_count}</h1>
    </div>
  );
}
