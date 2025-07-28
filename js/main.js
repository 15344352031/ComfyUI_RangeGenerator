import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "Comfy.RangeGenerator",
    
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "RangeGenerator") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function() {
                if (onNodeCreated) {
                    onNodeCreated.apply(this, arguments);
                }
                
                this.addWidget("text", "范围", "", (value) => {}, { multiline: true, readonly: true });
            };
            
            const onDrawBackground = nodeType.prototype.onDrawBackground;
            nodeType.prototype.onDrawBackground = function(ctx) {
                if (onDrawBackground) {
                    onDrawBackground.apply(this, arguments);
                }
                
                const icon = "🔢";
                ctx.font = "16px Arial";
                ctx.fillStyle = "#ffffff";
                ctx.fillText(icon, 10, 30);
            };
            
            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function(message) {
                if (onExecuted) {
                    onExecuted.apply(this, arguments);
                }
                
                // 更新索引为7，因为现在有8个输入参数
                // (range_start, range_end, step, allow_reverse, prefix, suffix, global_prefix, global_suffix)
                if (this.widgets && this.widgets[7] && message.range_string) {
                    this.widgets[7].value = message.range_string;
                }
            };
        }
    }
}); 