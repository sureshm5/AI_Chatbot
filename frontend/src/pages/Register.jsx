import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { register } from "../services/auth";

export default function Register(){

    const navigate = useNavigate();

    const [form,setForm] = useState({

        name:"",
        email:"",
        password:""

    });

    async function submit(){

        try{

            await register(form);

            alert("Registered Successfully");

            navigate("/login");

        }

        catch{

            alert("Registration Failed");

        }

    }

    return(

        <div className="h-screen flex justify-center items-center bg-slate-900">

            <div className="bg-slate-800 p-8 rounded-xl w-96">

                <h1 className="text-3xl text-white mb-6">

                    Register

                </h1>

                <input

                    placeholder="Name"

                    className="w-full p-3 mb-3 rounded"

                    onChange={e=>setForm({...form,name:e.target.value})}

                />

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

                    Register

                </button>

                <p className="text-center text-gray-400 mt-5">

                    Already have an account?{" "}

                    <span

                        onClick={() => navigate("/login")}

                        className="text-blue-500 cursor-pointer hover:underline"

                    >

                        Login

                    </span>

                </p>

            </div>

        </div>

    );

}