import {Navbar} from "@/components/layout/navbar/Navbar";
import {Sidebar} from "@/components/layout/sidebar/Sidebar";
import "./layout.scss"

export default function Layout ({ children }: Readonly<{ children: React.ReactNode }>) {
    return (
        <div className="app">
            <Navbar />
            <Sidebar />
            <main className="main-content">
                {children}
            </main>
        </div>
    )
}
