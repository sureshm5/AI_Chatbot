import api from "./api";

export const createConversation = async () => {
    const res = await api.post("/conversation/");
    return res.data;
};

export const getConversations = async () => {
    const res = await api.get("/conversation/");
    return res.data;
};

export const sendMessage = async (conversationId, message) => {

    const res = await api.post("/chat", {
        conversation_id: conversationId,
        message: message
    });

    return res.data;
};

export const getMessages = async (conversationId) => {

    const res = await api.get(
        `/conversation/${conversationId}`
    );

    return res.data;

};

export async function deleteConversation(id){

    const res = await api.delete(

        `/conversation/${id}`

    );

    return res.data;

}

export async function renameConversation(

    id,

    title

){

    const res = await api.put(

        `/conversation/${id}`,

        {

            title

        }

    );

    return res.data;

}