--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

-- Started on 2022-07-10 18:48:37

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
-- TOC entry 209 (class 1259 OID 16395)
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    id integer NOT NULL,
    nome character varying NOT NULL,
    login character varying NOT NULL,
    senha character varying NOT NULL,
    email character varying NOT NULL
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16436)
-- Name: cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.cliente ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.cliente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 210 (class 1259 OID 16400)
-- Name: estoque; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estoque (
    id integer NOT NULL,
    funcionario_id integer NOT NULL
);


ALTER TABLE public.estoque OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16467)
-- Name: estoque_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.estoque ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.estoque_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 211 (class 1259 OID 16403)
-- Name: estoque_produto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estoque_produto (
    estoque_id integer NOT NULL,
    produto_id integer NOT NULL,
    quantidade integer NOT NULL
);


ALTER TABLE public.estoque_produto OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16406)
-- Name: funcionario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.funcionario (
    id integer NOT NULL,
    nome character varying NOT NULL,
    login character varying NOT NULL,
    senha character varying NOT NULL,
    email character varying NOT NULL
);


ALTER TABLE public.funcionario OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16468)
-- Name: funcionario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.funcionario ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.funcionario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 213 (class 1259 OID 16411)
-- Name: pedido; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pedido (
    id integer NOT NULL,
    cliente_id integer NOT NULL,
    funcionario_id integer NOT NULL
);


ALTER TABLE public.pedido OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16469)
-- Name: pedido_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.pedido ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.pedido_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 214 (class 1259 OID 16414)
-- Name: pedido_produto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pedido_produto (
    pedido_id integer NOT NULL,
    produto_id integer NOT NULL,
    quantidade integer
);


ALTER TABLE public.pedido_produto OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16417)
-- Name: produto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produto (
    id integer NOT NULL,
    nome character varying NOT NULL,
    preco double precision NOT NULL
);


ALTER TABLE public.produto OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16470)
-- Name: produto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.produto ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.produto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 3201 (class 2606 OID 16423)
-- Name: pedido Pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT "Pedido_pkey" PRIMARY KEY (id);


--
-- TOC entry 3193 (class 2606 OID 16425)
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id);


--
-- TOC entry 3195 (class 2606 OID 16427)
-- Name: estoque estoque_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estoque
    ADD CONSTRAINT estoque_pkey PRIMARY KEY (id);


--
-- TOC entry 3197 (class 2606 OID 16429)
-- Name: estoque_produto estoque_produto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estoque_produto
    ADD CONSTRAINT estoque_produto_pkey PRIMARY KEY (estoque_id, produto_id);


--
-- TOC entry 3199 (class 2606 OID 16431)
-- Name: funcionario funcionario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (id);


--
-- TOC entry 3203 (class 2606 OID 16433)
-- Name: pedido_produto pedido_produto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido_produto
    ADD CONSTRAINT pedido_produto_pkey PRIMARY KEY (produto_id, pedido_id);


--
-- TOC entry 3205 (class 2606 OID 16435)
-- Name: produto produto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT produto_pkey PRIMARY KEY (id);


--
-- TOC entry 3207 (class 2606 OID 16442)
-- Name: estoque_produto estoque_id_estoque; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estoque_produto
    ADD CONSTRAINT estoque_id_estoque FOREIGN KEY (estoque_id) REFERENCES public.estoque(id) NOT VALID;


--
-- TOC entry 3208 (class 2606 OID 16447)
-- Name: pedido pedido_id_cliente; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_id_cliente FOREIGN KEY (cliente_id) REFERENCES public.cliente(id) NOT VALID;


--
-- TOC entry 3209 (class 2606 OID 16452)
-- Name: pedido pedido_id_funcionario; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_id_funcionario FOREIGN KEY (funcionario_id) REFERENCES public.funcionario(id) NOT VALID;


--
-- TOC entry 3210 (class 2606 OID 16457)
-- Name: pedido_produto pedido_produto_pedido_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido_produto
    ADD CONSTRAINT pedido_produto_pedido_id FOREIGN KEY (pedido_id) REFERENCES public.pedido(id) NOT VALID;


--
-- TOC entry 3211 (class 2606 OID 16462)
-- Name: pedido_produto pedido_produto_produto_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido_produto
    ADD CONSTRAINT pedido_produto_produto_id FOREIGN KEY (produto_id) REFERENCES public.produto(id) NOT VALID;


--
-- TOC entry 3206 (class 2606 OID 16437)
-- Name: estoque_produto produto_id_estoque; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estoque_produto
    ADD CONSTRAINT produto_id_estoque FOREIGN KEY (produto_id) REFERENCES public.produto(id) NOT VALID;


-- Completed on 2022-07-10 18:48:37

--
-- PostgreSQL database dump complete
--

