--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-07-18 21:35:56

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
-- TOC entry 216 (class 1259 OID 30158)
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(80) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 30157)
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_id_seq OWNER TO postgres;

--
-- TOC entry 4844 (class 0 OID 0)
-- Dependencies: 215
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- TOC entry 4688 (class 2604 OID 30161)
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- TOC entry 4837 (class 0 OID 30158)
-- Dependencies: 216
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, username, password) FROM stdin;
30	Cerberus35	scrypt:32768:8:1$Zgd6l3uxOuDUvFsb$31d3f1f70737eb47ee5ac4a79c92d94bc788e6b7d3b3192a469244878d77ace2ff7a2f5bbf556ad58702ba7976ecf077908d5a71bc09b2b892f871da329d37b2
31	LilPaaaaRRR	scrypt:32768:8:1$VZ4twtE96JsUxGeq$a003381f5b66b5e1d1123dff9c0efc543e727a7a344661ee50549ba5c067ac8ef95b14bdd2a589785c183c285b9594b7f4f345ad1e8a2c651dcef3980da4e79a
26	Ccody	scrypt:32768:8:1$vJoa30M2YDpjhQ7r$99fb33ff589005b51f94e26dca761b625c1f177c522c0dd08fb9c82f2b7162ef9789e63a3e6845165b43f6e5ad0fee56e21b72efc2156cb8ca917463f0236842
28	Буркарь	scrypt:32768:8:1$67WGjolOrH5iX2FK$3ea2863f7c0a14ec92ea91647202a7d52cd76421bcaf7d1a73fff7812cda2e33d3b96b6d8634ab50d111a874315cea63ba711c34bdd9ac38d4772a514b5e093a
29	ГнездовОлег	scrypt:32768:8:1$e66LSzSgkjwj7nco$78135ce1c9cc78879cd98fb40a27767d9db4eb50c12265d4ba2f06f916a6ba2115847806203eedd5b7a124adb38c90db8f68b22a7ddbb35fc67438b19f86c67c
\.


--
-- TOC entry 4846 (class 0 OID 0)
-- Dependencies: 215
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 31, true);


--
-- TOC entry 4690 (class 2606 OID 30163)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- TOC entry 4692 (class 2606 OID 30165)
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- TOC entry 4843 (class 0 OID 0)
-- Dependencies: 216
-- Name: TABLE "user"; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public."user" TO ryota;


--
-- TOC entry 4845 (class 0 OID 0)
-- Dependencies: 215
-- Name: SEQUENCE user_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public.user_id_seq TO ryota;


-- Completed on 2024-07-18 21:35:56

--
-- PostgreSQL database dump complete
--

