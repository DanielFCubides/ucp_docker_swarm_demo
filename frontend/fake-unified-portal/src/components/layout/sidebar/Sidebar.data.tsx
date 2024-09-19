import {IconChartBar, IconHash, IconHome, IconNotes} from "@tabler/icons-react"
export const SidebarData = [
    {
        label: "Home",
        icon: <IconHome />,
        active: true,
    },
    {
        label: "Solutions",
        icon: <IconNotes/>,
    },
    {
        label: "Numbers and senders",
        icon: <IconHash />,
        arrow: true,
    },
    {
        label: "Reports",
        icon: <IconChartBar />,
        arrow: true,
    }
]
