import './Visits.scss'
import {Counter} from "@/app/(home)/components/counter/Counter";
import {Visitors} from "@/services/reports";

export const Visits = ({visits} : {visits: Visitors}) => {
    return (
        <div className="visits-container">
            <h1>Visits count</h1>
            <h1 className="visit-counter"><Counter initialValue={0} targetValue={visits.visit_count} /></h1>
            <h1>Local visits count</h1>
            <h1 className="visit-counter"><Counter initialValue={0} targetValue={visits.local_visit_count} /></h1>
        </div>
    )
}
