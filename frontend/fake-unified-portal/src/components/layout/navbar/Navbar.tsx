import "./Navbar.scss"
import {IconChevronUp, IconExternalLink, IconUserCircle} from "@tabler/icons-react";
export const Navbar: React.FC = () => {
    return (
        <>
            <nav className="navbar">
                <div className="user-info">
                    <IconUserCircle/>
                    <p>Test Account</p>
                    <IconChevronUp/>
                </div>
            </nav>
            <div className="navbar-info">
                <p>
                    If you can’t find what you need, visit our <span className="link-fake">legacy portal <IconExternalLink /></span>
                    . Soon, everything will be accessible through My Telesign.</p>
            </div>
        </>
    )
}
