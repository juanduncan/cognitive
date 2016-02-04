/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "tx_valve_impl.h"




using namespace std;

namespace gr {
  namespace COWN {

    tx_valve::sptr
    tx_valve::make()
    {
      return gnuradio::get_initial_sptr
        (new tx_valve_impl());
    }

    /*
     * The private constructor
     */
    tx_valve_impl::tx_valve_impl()
      : gr::block("tx_valve",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(gr_complex)))
    {
	set_tag_propagation_policy(block::TPP_ALL_TO_ALL);
	transmit_tail = false;
	Number_of_last_samples =0;
	}

    /*
     * Our virtual destructor.
     */
    tx_valve_impl::~tx_valve_impl()
    {
    }

    void
    tx_valve_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {      if (noutput_items >1024){
           ninput_items_required[0] = 0;
           }else{
			  ninput_items_required[0] = 0; 
			  }
                 
    }

    int
    tx_valve_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];
        gr_complex *out = (gr_complex*) output_items[0];

		
		uint64_t abs_start = nitems_read(0) ;
        uint64_t abs_end = nitems_read(0) + noutput_items ;
		get_tags_in_range(d_tags, 0, abs_start,abs_end);
		 //if (d_tags.size()) {
			 //std::sort(d_tags.begin(), d_tags.end(), gr::tag_t::offset_compare);
			 //gr::tag_t el =  d_tags.front();
			 ////cout << "dtags " << el.key << "   " << el.value   << "\t";
			 //cout << "size " << d_tags.size()   << "\t";
			 //cout << "offset " << el.offset   << "\t";
			 //el = d_tags[2];
			 ////pmt::pmt_t packet_length = el.value;
			 //packet_length = pmt::to_long(el.value);
			 //cout << "dtags " << el.key << " " <<   packet_length  << "\t";
			 //cout<<  "nitems_read" << ": "<<  nitems_read(0)<< "\t"  ;
			 //cout<<  "nitems_written" << ": "<<  nitems_written(0)<< "\t"  ;
			 //cout<<  "Time W" << ": "<<  nitems_written(0)/5e5<< "\t"  ;
			 ////cout<<  "Ratio" << ": "<<  nitems_read(0)/nitems_written(0)*1.00 << "\t"  ;
			 //cout << "ninput: "  << ninput_items[0]  << "\t";
			 //cout << "noutput: "  << noutput_items  << endl;
		 //}else{ 
			 //cout << "\tsize " << d_tags.size()   << "\t";
			 //cout << " packet_length" << "   " <<   packet_length  << "\t";
			 //cout<<  "nitems_read(0)" << ": "<<  nitems_read(0)<< "\t"  ;
			 //cout<<  "nitems_written" << ": "<<  nitems_written(0)<< "\t"  ;
			 //cout<<  "Time W" << ": "<<  nitems_written(0)/5e5<< "\t"  ;
			 ////cout<<  "Ratio" << ": "<<  nitems_read(0)/nitems_written(0)*1.00 << "\t"  ;
			 //cout << "ninput: "  << ninput_items[0]  << "\t";
			 //cout << "noutput: "  << noutput_items  << endl;
	      //}
         
         int items_to_produce;

         //if(packet_length >= noutput_items) {
			 //packet_length-=noutput_items;
			 //items_to_produce = noutput_items;
		 //}else if(packet_length < noutput_items){
			 //packet_length = 0 ;
			 //items_to_produce = noutput_items - packet_length;  
	     //}
        //for(int i=0; i <1; i++ ){cout << "PUTA "<< items_to_produce<< " no"<< noutput_items << " ";} 
          
        
        if (ninput_items[0] <  noutput_items){ 
			for(int i=0; i <ninput_items[0]; i++ ){out[i] = in[i];}
			for(int i=ninput_items[0]; i <noutput_items; i++ ){
				out[i] = gr_complex(0,0); 
			}
			consume_each(ninput_items[0]);
		}else{
			for(int i=0; i <noutput_items; i++ ){out[i] = in[i];}
			consume_each(noutput_items);
		}
        
        
			 
				
		//if(!transmit_tail){
			//if (ninput_items[0] >= noutput_items){
				//for(int i=0; i <noutput_items; i++ ){out[i] = in[i];}
				//if (ninput_items[0] > noutput_items+1024){
					//consume_each(noutput_items);
				//}else{
					//transmit_tail = true;
					//Number_of_last_samples = ninput_items[0];
				//}
			//}else{
				//for(int i=0; i <ninput_items[0]; i++ ){out[i] = in[i];}
				//for(int i=ninput_items[0]; i <noutput_items; i++ ){
					//out[i] = gr_complex(0,0); 
				//}
				//transmit_tail = true;
				//Number_of_last_samples = ninput_items[0];
			//}
		//}else{
			//for(int i=0; i <noutput_items; i++ ){
					//out[i] = gr_complex(0,0);
			//}
			//if (ninput_items[0] > Number_of_last_samples){
				//consume_each(Number_of_last_samples);
				//transmit_tail = false;
			//}
		//}
		 
			
			 
        return noutput_items;
    }

  } /* namespace COWN */
} /* namespace gr */

