import { Elysia } from "elysia";
import { authen } from "./api/v1/auth/controllers";

export const app = new Elysia().listen(8000);

console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`
);

app.use(authen);