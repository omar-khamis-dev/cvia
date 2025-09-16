"use client";
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";


export default function ChatPage() {
const [msg, setMsg] = useState("");
const { mutate, data, isPending } = useMutation({
mutationFn: async (body: { message: string }) => {
const r = await fetch("/api/v1/chat", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(body),
});
return r.json();
},
});


return (
<main className="mx-auto max-w-2xl p-4">
<div className="h-80 overflow-y-auto rounded-lg border p-3 mb-3 shadow-sm">
{data?.reply ?? "Ask me anything about your CV!"}
</div>
<div className="flex">
<input
className="flex-1 rounded-l-lg border p-2"
value={msg}
onChange={(e) => setMsg(e.target.value)}
placeholder="Type …"
/>
<button
onClick={() => mutate({ message: msg })}
disabled={isPending || !msg.trim()}
className="rounded-r-lg bg-blue-600 px-4 py-2 text-white disabled:opacity-50"
>Send</button>
</div>
</main>
);
}