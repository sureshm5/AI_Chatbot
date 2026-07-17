import { uploadPDF } from "../services/upload";
import { useNavigate } from "react-router-dom";

export default function Header() {

    const navigate = useNavigate();

    async function upload(e) {

        const file = e.target.files[0];

        if (!file) return;

        try {

            const res = await uploadPDF(file);

            alert(res.status);

        }

        catch {

            alert("Upload Failed");

        }

    }

    function logout() {

        localStorage.removeItem("token");

        navigate("/login");

    }

    return (

        <div className="flex justify-between items-center border-b border-slate-700 p-5">

            <div>

                <h1 className="text-3xl font-bold text-white">

                    Enterprise AI Assistant

                </h1>

                <p className="text-gray-400">

                    Powered by GPT-OSS-20B

                </p>

            </div>

            <div className="flex items-center gap-3">

                <label className="bg-green-600 px-4 py-2 rounded cursor-pointer hover:bg-green-700">

                    Upload PDF

                    <input

                        type="file"

                        accept=".pdf"

                        hidden

                        onChange={upload}

                    />

                </label>

                <button

                    onClick={logout}

                    className="bg-red-600 px-4 py-2 rounded hover:bg-red-700"

                >

                    Logout

                </button>

            </div>

        </div>

    );

}