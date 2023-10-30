import Elysia from "elysia";


export const authen = (app: Elysia) =>
    app.group('/auth', (app) =>
        app.post('/signup', () => {
            return "expected signup";
        })
        .post('/login', () => {
            return 'exepcted login';
        })
    )