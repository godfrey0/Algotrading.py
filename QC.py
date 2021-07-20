Class GeekyOrangeLion(QCAlgorithm):
    
    def Initialize(self):
        self.SetStartDate(2018, 1, 1)
        self.SetCash(100000)
        self.long_list = []
        self.short_list = []
        
        #self.rsi = self.RSI("EURUSD", 14)
        #self.macd = self.MACD("EURUSD",12,26,9,MovingAverageType.Exponential,Resolution.Daily)
        
        self.stop=False
        self.equities=["AAPL","NVDA","LUV","PFE","MSFT"]
        self.AddEquity("AAPL", Resolution.Daily)
        self.AddEquity("NVDA", Resolution.Daily)
        self.AddEquity("LUV", Resolution.Daily)
        self.AddEquity("PFE", Resolution.Daily)
        self.AddEquity("MSFT", Resolution.Daily)

    def OnData(self, data):
        
        #if self.stop:
        #    return
        
        equities=self.equities
        
        for equity in equities:
            #self.Debug("The equity is running")
            equity_data=self.History([equity],50,Resolution.Daily)
            MA50_Pre = equity_data.close[0:50].mean()
            MA20_Pre = equity_data.close[30:50].mean()
            MA50_Current = equity_data.close[1:51].mean()
            MA20_Current = equity_data.close[31:51].mean()
             
            
            #First Trade
            #entry
            
            #
            if equity not in self.long_list and equity not in self.short_list:
                self.Debug("found equity" + str(equity))
                #checking Bullish Crossover
                if MA20_Pre<MA50_Pre and MA20_Current>MA50_Current:
                    #self.Debug("checking long condition")
                    if equity == "AAPL":
                        self.SetHoldings(equity, 0.01539689)
                    if equity == "PFE":
                        self.SetHoldings(equity, 0.10075731)
                    if equity == "LUV":
                        self.SetHoldings(equity, 0.01797449)
                    if equity == "NVDA":
                        self.SetHoldings(equity, 0.67555967)
                    if equity == "MSFT":
                        self.SetHoldings(equity, 0.19031164)
                    self.long_list.append(equity)
                #checking Bearish Crossover    
                if MA20_Pre>MA50_Pre and MA20_Current<MA50_Current:
                    if equity == "AAPL":
                        self.SetHoldings(equity, 0.01539689)
                    if equity == "PFE":
                        self.SetHoldings(equity, 0.10075731)
                    if equity == "LUV":
                        self.SetHoldings(equity, 0.01797449)
                    if equity == "NVDA":
                        self.SetHoldings(equity, 0.67555967)
                    if equity == "MSFT":
                        self.SetHoldings(equity, 0.19031164)
                    self.short_list.append(equity)
            #exit and again entry
            if equity in self.long_list:
                #checking Bearish Crossover
                if MA20_Pre>MA50_Pre and MA20_Current<MA50_Current:
                    if equity == "AAPL":
                        self.SetHoldings(equity, 0.01539689)
                    if equity == "PFE":
                        self.SetHoldings(equity, 0.10075731)
                    if equity == "LUV":
                        self.SetHoldings(equity, 0.01797449)
                    if equity == "NVDA":
                        self.SetHoldings(equity, 0.67555967)
                    if equity == "MSFT":
                        self.SetHoldings(equity, 0.19031164)
                    self.long_list.remove(equity)
                    self.short_list.append(equity)
            
            if equity in self.short_list:
                #Checking Bullish Crossover
                if MA20_Pre<MA50_Pre and MA20_Current>MA50_Current:
                    if equity == "AAPL":
                        self.SetHoldings(equity, 0.01539689)
                    if equity == "PFE":
                        self.SetHoldings(equity, 0.10075731)
                    if equity == "LUV":
                        self.SetHoldings(equity, 0.01797449)
                    if equity == "NVDA":
                        self.SetHoldings(equity, 0.67555967)
                    if equity == "MSFT":
                        self.SetHoldings(equity, 0.19031164)
                    self.short_list.remove(equity)
                    self.long_list.append(equity)
                    
            
        #if self.Portfolio.Cash<0.1*10000:
         #       self.stop=True
         #       self.Liquidate()
        ''' OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        '''
      
        # Check if we're not invested and then put portfolio 100% in the SPY ETF.      
        #if not self.Portfolio.Invested:
         #  self.SetHoldings("SPY", 1)

       
         
        