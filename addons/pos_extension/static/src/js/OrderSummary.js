odoo.define('pos_extension.OrderSummary', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.OrderSummary');
    const Registries = require('point_of_sale.Registries');
    const { float_is_zero } = require('web.utils');

    class OrderSummary extends PosComponent {

        getSubTotalPrice() {
            let subtotal = 0.0
            for (let i=0; i < this.props.order.orderlines.length; i++){
                if(this.props.order.orderlines[i].product.id !== this.props.order.pos.config['discount_product_id'][0]){
                    subtotal += this.props.order.orderlines[i].price * this.props.order.orderlines[i].quantity
                }
            }
            console.log(subtotal)
            return this.env.pos.format_currency(subtotal)
        }

    }
    OrderSummary.template = 'OrderSummary';

    Registries.Component.add(OrderSummary);

    return OrderSummary;
});
