from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
RAW_PATH = BASE_DIR / "Deputados_Ano-2025.csv"
OUT_DIR = BASE_DIR / "data" / "clean_data"
OUT_PATH = OUT_DIR / "deputados_2025_clean.csv"
DICT_PATH = BASE_DIR / "docs" / "data_dictionary_deputado.md"

VALUE_COLUMNS = ["vlrDocumento", "vlrGlosa", "vlrLiquido", "vlrRestituicao"]
INT_COLUMNS = [
    "ideCadastro",
    "nuCarteiraParlamentar",
    "nuLegislatura",
    "codLegislatura",
    "numSubCota",
    "numEspecificacaoSubCota",
    "indTipoDocumento",
    "numMes",
    "numAno",
    "numParcela",
    "numLote",
    "numRessarcimento",
    "nuDeputadoId",
    "ideDocumento",
]
DATE_COLUMNS = ["datEmissao", "datPagamentoRestituicao"]


def load_raw(path: Path = RAW_PATH) -> pd.DataFrame:
    return pd.read_csv(
        path,
        sep=";",
        quotechar='"',
        encoding="utf-8",
        engine="python",
        dtype=str,
    )


def clean_deputados(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Normalize strings and missing values
    for col in df.columns:
        df[col] = df[col].astype("string").str.strip()
    df = df.replace({"": pd.NA, "NaN": pd.NA, "nan": pd.NA, "NULL": pd.NA, "None": pd.NA})

    # Parse numeric values
    for col in VALUE_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in INT_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    # Parse dates
    for col in DATE_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    df = df.drop_duplicates()
    return df


def _dtype_to_label(dtype) -> str:
    if pd.api.types.is_integer_dtype(dtype):
        return "int"
    if pd.api.types.is_float_dtype(dtype):
        return "float"
    if pd.api.types.is_datetime64_any_dtype(dtype):
        return "datetime"
    return "string"


def write_data_dictionary(df: pd.DataFrame, path: Path = DICT_PATH) -> None:
    descriptions = {
        "txNomeParlamentar": "Nome parlamentar do deputado.",
        "cpf": "CPF do parlamentar (pode estar ausente).",
        "ideCadastro": "Identificador do cadastro do parlamentar.",
        "nuCarteiraParlamentar": "Numero da carteira parlamentar.",
        "nuLegislatura": "Numero da legislatura.",
        "sgUF": "Sigla da UF do parlamentar.",
        "sgPartido": "Sigla do partido.",
        "codLegislatura": "Codigo da legislatura.",
        "numSubCota": "Codigo da subcota de despesa.",
        "txtDescricao": "Descricao da despesa (subcota).",
        "numEspecificacaoSubCota": "Codigo da especificacao da subcota.",
        "txtDescricaoEspecificacao": "Descricao da especificacao da subcota.",
        "txtFornecedor": "Nome do fornecedor.",
        "txtCNPJCPF": "CNPJ/CPF do fornecedor.",
        "txtNumero": "Numero do documento.",
        "indTipoDocumento": "Indicador do tipo de documento.",
        "datEmissao": "Data de emissao do documento.",
        "vlrDocumento": "Valor do documento.",
        "vlrGlosa": "Valor glosado.",
        "vlrLiquido": "Valor liquido.",
        "numMes": "Mes de referencia da despesa.",
        "numAno": "Ano de referencia da despesa.",
        "numParcela": "Numero da parcela (quando aplicavel).",
        "txtPassageiro": "Nome do passageiro (quando aplicavel).",
        "txtTrecho": "Trecho da viagem (quando aplicavel).",
        "numLote": "Numero do lote.",
        "numRessarcimento": "Numero do ressarcimento.",
        "datPagamentoRestituicao": "Data de pagamento da restituicao.",
        "vlrRestituicao": "Valor da restituicao.",
        "nuDeputadoId": "Identificador do deputado.",
        "ideDocumento": "Identificador do documento.",
        "urlDocumento": "URL do documento digital.",
    }

    lines = [
        "# Data Dictionary - Deputados 2025",
        "",
        "Este dicionario descreve as colunas do arquivo limpo.",
        "",
        "| Coluna | Tipo | Nulos | Descricao |",
        "| --- | --- | --- | --- |",
    ]

    for col in df.columns:
        dtype_label = _dtype_to_label(df[col].dtype)
        null_count = int(df[col].isna().sum())
        desc = descriptions.get(col, "Sem descricao.")
        lines.append(f"| {col} | {dtype_label} | {null_count} | {desc} |")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    df = load_raw()
    df_clean = clean_deputados(df)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(OUT_PATH, index=False)
    write_data_dictionary(df_clean)


if __name__ == "__main__":
    main()

import pandas as pd

caminho_2025 = "/Users/luigiajello/Downloads/5 semestre/extracao_preparacao_dados/data_extraction-course/Deputados_Ano-2025.csv"
pd.read_csv(caminho_2025, sep=";", quotechar='"', encoding="utf-8", engine="python")

