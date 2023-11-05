import { Elysia, t } from 'elysia';
import { supabase } from '../../../libs/supabase';
// import { cookie } from '@elysiajs/cookie';

export const authen = (app: Elysia) =>
  app.group(
    '/auth',
    (app) =>
      app
        .setModel({
          sign: t.Object({
            email: t.String({
              format: 'email',
            }),
            password: t.String({
              minLength: 8,
            }),
          }),
        })
        .post(
          '/signup',
          async ({ body }) => {
            const { data, error } = await supabase.auth.signUp(body);

            if (error) return error;

            return data.user;
          },
          {
            schema: {
              body: 'sign',
            },
          }
        )
        .post(
          '/login',
          async ({ body }) => {
            const { data, error } = await supabase.auth.signInWithPassword(
              body
            );

            if (error) return error;

            return data.user;
          },
          {
            schema: {
              body: 'sign',
            },
          }
        )
    //   .get('/refresh', async ({ setCookie, cookie: { refresh_token } }) => {
    //     const { data, error } = await supabase.auth.refreshSession({
    //       refresh_token,
    //     });

    //     if (error) return error;

    //     setCookie('refresh_token', data.session!.refresh_token);

    //     return data.user;
    //   })
  );
