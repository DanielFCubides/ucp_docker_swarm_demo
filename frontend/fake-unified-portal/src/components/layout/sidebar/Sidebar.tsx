import {SidebarData} from "@/components/layout/sidebar/Sidebar.data";
import {IconCaretDownFilled, IconChevronRight} from "@tabler/icons-react";
import "./Sidebar.scss";
import Image from "next/image";
import BrandIcon from "./../../../public/brand.png"

export const Sidebar: React.FC = () => {
    return (
        <aside className="sidebar">
            <div className="sidebar-header">
                <Image src={BrandIcon} alt="brand-icon" />
                <h1>zzz-Team 2 Portal Testing</h1>
                <p className="sidebar-account">Full-service account</p>
                <div className="sidebar-user">
                    Jhoy Account
                    <IconCaretDownFilled />
                </div>
            </div>
            <div className="sidebar-main">
                <ul>
                    {SidebarData.map((item) => (
                        <li
                            className={`sidebar-item${item?.active ? " active" : ""}`}
                            key={item.label}
                        >
                            {item.icon}
                            <span>{item.label}</span>
                            {item?.arrow ? <IconChevronRight /> : null}
                        </li>
                    ))}
                </ul>
            </div>
        </aside>
    )
}
