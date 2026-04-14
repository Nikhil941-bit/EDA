{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f94bd6d9-6f7c-4e72-818f-c8e6f7dff112",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-03-12 05:56:30.980 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:30.982 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:30.983 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.023 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.024 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.024 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.025 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.026 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.026 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.027 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.027 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.028 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.028 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.029 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.030 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.030 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.051 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.051 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.052 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.052 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-12 05:56:31.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "st.title(\"Superstore EDA Dashboard\")\n",
    "\n",
    "# Load dataset\n",
    "df = pd.read_csv(\"train.csv\")\n",
    "\n",
    "# Convert date\n",
    "df[\"Order Date\"] = pd.to_datetime(df[\"Order Date\"], dayfirst=True)\n",
    "\n",
    "# KPI metrics\n",
    "total_sales = df[\"Sales\"].sum()\n",
    "total_orders = df[\"Order ID\"].nunique()\n",
    "avg_sales = df[\"Sales\"].mean()\n",
    "\n",
    "col1, col2, col3 = st.columns(3)\n",
    "\n",
    "col1.metric(\"Total Sales\", f\"${total_sales:,.0f}\")\n",
    "col2.metric(\"Avg Sales per Order\", f\"${avg_sales:,.2f}\")\n",
    "col3.metric(\"Total Orders\", total_orders)\n",
    "\n",
    "# Monthly sales trend\n",
    "monthly_sales = df.groupby(df[\"Order Date\"].dt.to_period(\"M\"))[\"Sales\"].sum().reset_index()\n",
    "monthly_sales[\"Month\"] = monthly_sales[\"Order Date\"].astype(str)\n",
    "\n",
    "fig = px.line(monthly_sales, x=\"Month\", y=\"Sales\", title=\"Monthly Sales Trend\")\n",
    "st.plotly_chart(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74c7a375-c716-4ee5-85ef-04f7ebf2116b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
