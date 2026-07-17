import api from "./api";

export async function uploadPDF(file) {

    const formData = new FormData();

    formData.append("file", file);

    const res = await api.post(

        "/upload/pdf",

        formData,

        {

            headers: {

                "Content-Type": "multipart/form-data"

            }

        }

    );

    return res.data;

}