import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { login } from "../services/auth";

export default function Login(){

    const navigate = useNavigate();

    const [form,setForm] = useState({

        email:"",
        password:""

    });

    async function submit(){

        try{

            const response = await login(form);

            localStorage.setItem(

                "token",

                response.access_token

            );

            alert("Login Successful");

            navigate("/");

        }

        catch{

            alert("Invalid Credentials");

        }

    }

    return(

        <div className="h-screen flex justify-center items-center bg-slate-900">

            <div className="bg-slate-800 p-8 rounded-xl w-96">

                <h1 className="text-3xl text-white mb-6">

                    Login

                </h1>

                <input

                    placeholder="Email"

                    className="w-full p-3 mb-3 rounded"

                    onChange={e=>setForm({...form,email:e.target.value})}

                />

                <input

                    type="password"

                    placeholder="Password"

                    className="w-full p-3 mb-5 rounded"

                    onChange={e=>setForm({...form,password:e.target.value})}

                />

                <button

                    onClick={submit}

                    className="w-full bg-blue-600 p-3 rounded text-white"

                >

                    Login

                </button>
                <p className="text-center text-gray-400 mt-5">

                    Don't have an account?{" "}

                    <span

                        onClick={() => navigate("/register")}

                        className="text-blue-500 cursor-pointer hover:underline"

                    >

                        Sign Up

                    </span>

                </p>

            </div>

        </div>

    );

}