import { useState } from "react";
import axios from "axios";

export default function AdminLogin() {
    const[username, setUsername] = useState("");
    const[password, setPassword] = useState("");
    const[msg, setMsg] = useState("");

    const handleLogin = async () => {
        try {
            const res = await axios.post("http://127.0.0.1:8000/api/admin/login/", {
                username,
                password
            });
            localStorage.setItem("adminToken", res.data.tokens.access);
            setMsg("Login Successful");
            window.location.href = "/admin/dashboard";
        } catch (err) {
            setMsg("Inavalid Credentials");
        }
    };
  


return (
    <div style={{ width: "300px", margin: "auto", paddingTop: "50px" }}>
        <h2>Admin Login</h2>
        <input className="form-control" placeholder="Username" onChange={(e) => setUsername(e.target.value)}/><br/>
        <input className="form-control" placeholder="Password" onChange={(e) => setUsername(e.target.value)}/><br/>
        <button className="btn btn-primary" onClick={handleLogin}></button>
        <p>{msg}</p>
    </div>
);
}