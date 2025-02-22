# XRPL Last 500 Ledgers Fetcher

## Overview
The XRPL Last 500 Ledgers Fetcher is a tool designed to retrieve and analyze transaction data from the **XRP Ledger (XRPL)**. By connecting directly to the XRPL JSON-RPC server, it efficiently fetches data from the **last 500 validated ledgers**, extracting transaction details and measuring performance metrics such as total time taken and average retrieval speed.

## Key Features
- **Live Data Retrieval**: Connects to XRPL’s JSON-RPC server to fetch real-time ledger data.
- **Transaction Extraction**: Retrieves all transactions from each of the last 500 validated ledgers.
- **Performance Monitoring**: Measures the total time taken and the average time per ledger.

## Example Output
For the latest 500 ledgers, the script produces the following output:

```
Total time spent fetching all ledgers: 363.1298 seconds
Number of ledgers fetched: 500 ledgers
Average time taken to fetch each ledger: 0.7263 seconds
```

## How It Works
1. The script first retrieves the **latest validated ledger index** from the XRPL network.
2. It iterates over the **last 500 ledgers**, fetching **transaction data** from each one.
3. It calculates the **total time taken** to process all ledgers and determines the **average time per ledger**.
4. The transaction data is stored in a list for potential further processing or analysis.

## Why It Matters
Understanding ledger transaction flow is crucial for developers, analysts, and blockchain enthusiasts looking to monitor network activity, analyze trends, and optimize XRPL-related applications. This tool provides an efficient method to retrieve and analyze large-scale ledger data in real time.

## Conclusion
The XRPL Last 500 Ledgers Fetcher is a reliable solution for accessing recent transaction data from the XRP Ledger. With its ability to extract real-time ledger insights and track performance metrics, it serves as a valuable tool for blockchain research and analytics.

