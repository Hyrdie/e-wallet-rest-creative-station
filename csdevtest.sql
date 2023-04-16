--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6 (Homebrew)
-- Dumped by pg_dump version 14.6 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: transaction_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transaction_log (
    id_user integer NOT NULL,
    transaction character varying NOT NULL,
    amount integer NOT NULL
);


ALTER TABLE public.transaction_log OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(100) NOT NULL,
    password character varying(100) NOT NULL,
    email character varying(100) NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_balance; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_balance (
    id_user integer NOT NULL,
    balance integer NOT NULL
);


ALTER TABLE public.users_balance OWNER TO postgres;

--
-- Name: users_balance_id_user_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_balance_id_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_balance_id_user_seq OWNER TO postgres;

--
-- Name: users_balance_id_user_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_balance_id_user_seq OWNED BY public.users_balance.id_user;


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: users_token; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_token (
    id_user integer NOT NULL,
    access_token character varying NOT NULL
);


ALTER TABLE public.users_token OWNER TO postgres;

--
-- Name: users_token_id_user_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_token_id_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_token_id_user_seq OWNER TO postgres;

--
-- Name: users_token_id_user_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_token_id_user_seq OWNED BY public.users_token.id_user;


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: users_balance id_user; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_balance ALTER COLUMN id_user SET DEFAULT nextval('public.users_balance_id_user_seq'::regclass);


--
-- Name: users_token id_user; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_token ALTER COLUMN id_user SET DEFAULT nextval('public.users_token_id_user_seq'::regclass);


--
-- Data for Name: transaction_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transaction_log (id_user, transaction, amount) FROM stdin;
1	test	5000
1	test	5000
1	test	5000
1	test	0
1	test	0
1	test	5000
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, password, email) FROM stdin;
1	adiva	$2b$12$dNBNnWmUsGuo/j2CJC4C/eruWnbkNMXqi5dR97Vlwzl7gag5wV4rK	admin@gmail.com
2	test	$2b$12$J4sPDgM1aUn41BYOriun1egP7aKMHFPDF3XpBWY8L2PlT/lRIybWW	test@gmail.com
4	test1	$2b$12$y6M4/C49I1hQkvgS0ZGz7eOLT6aH25C1zXuwxBuyly2xjRU0q666q	test1@gmail.com
\.


--
-- Data for Name: users_balance; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_balance (id_user, balance) FROM stdin;
1	0
4	10000
\.


--
-- Data for Name: users_token; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_token (id_user, access_token) FROM stdin;
1	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZGl2YSIsImVtYWlsIjoiYWRtaW5AZ21haWwuY29tIiwiZXhwIjoxNjgxNjI0NzAyfQ.Zg6bSoTpSIJLmh1k9WJkAy8h-yaKj_otRxkLh6eamg4
2	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSIsImV4cCI6MTY4MTYzMTk4M30.DnWiL2YON4h9UGmqRWMSRXkO-pGsaDkl-utnyBLjo1Y
4	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwidXNlcm5hbWUiOiJ0ZXN0MSIsImVtYWlsIjoidGVzdDFAZ21haWwuY29tIiwiZXhwIjoxNjgxNjY2MzU3fQ.23FBLVx__goowXaYDD-Gx2jzfURnAVA_keeeYAUcJb4
\.


--
-- Name: users_balance_id_user_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_balance_id_user_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 4, true);


--
-- Name: users_token_id_user_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_token_id_user_seq', 1, false);


--
-- Name: users_balance users_balance_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_balance
    ADD CONSTRAINT users_balance_pkey PRIMARY KEY (id_user);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users_token users_token_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_token
    ADD CONSTRAINT users_token_pkey PRIMARY KEY (id_user);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- PostgreSQL database dump complete
--

