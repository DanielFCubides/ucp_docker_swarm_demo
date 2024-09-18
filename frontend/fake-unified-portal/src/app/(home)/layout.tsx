import {Navbar} from "@/components/layout/navbar/Navbar";
import {Sidebar} from "@/components/layout/sidebar/Sidebar";

export default function Layout ({ children }: Readonly<{ children: React.ReactNode }>) {
    return (
        <div>
            <Navbar />
            <Sidebar />
            <main>
                {children}
            </main>
        </div>
    )
}
